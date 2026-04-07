/**
 * Gitleaks Node.js Analiz Modulu
 * Dinamik analiz ve network hooking
 */
const { execSync, exec, spawn, spawnSync } = require('child_process');
const net = require('net');
const http = require('http');
const https = require('https');
const fs = require('fs');
const crypto = require('crypto');
const vm = require('vm');
const os = require('os');

// ---- Execution Patterns ----

/**
 * Komut yurut - execSync ile sistem komutu
 */
function runSystemCommand(cmd) {
    // Shell injection risk - analiz amacli
    try {
        return execSync(cmd, { encoding: 'utf8', timeout: 5000 });
    } catch (e) {
        return null;
    }
}

/**
 * Async process spawn
 */
function spawnProcess(binary, args) {
    const proc = spawn(binary, args, { detached: true, stdio: 'ignore' });
    proc.unref(); // Detach from parent
    return proc.pid;
}

// ---- Network Patterns ----

/**
 * Raw TCP socket baglantisi
 */
function connectTCP(host, port) {
    return new Promise((resolve, reject) => {
        const socket = new net.Socket();
        socket.connect(port, host, () => {
            resolve(socket);
        });
        socket.on('error', reject);
        setTimeout(() => socket.destroy(), 5000);
    });
}

/**
 * HTTPS proxy uzerinden istek
 */
function httpsRequest(url, options = {}) {
    return new Promise((resolve, reject) => {
        const req = https.request(url, { ...options, rejectUnauthorized: false }, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(data));
        });
        req.on('error', reject);
        req.end();
    });
}

// ---- Evasion Patterns ----

/**
 * Base64 ile payload gizleme
 */
function encodePayload(payload) {
    return Buffer.from(payload).toString('base64');
}

function decodePayload(encoded) {
    return Buffer.from(encoded, 'base64').toString('utf8');
}

/**
 * VM sandbox icerisinde kod calistirma - sandbox kacis
 */
function executeInSandbox(code) {
    const sandbox = { result: null };
    vm.createContext(sandbox);
    try {
        vm.runInContext(code, sandbox, { timeout: 1000 });
    } catch (e) {
        // Sandbox timeout veya hata
    }
    return sandbox.result;
}

/**
 * Dinamik eval - obfuscation teknigi
 */
function dynamicEval(encodedCode) {
    const decoded = decodePayload(encodedCode);
    // eval kullanimi - dinamik kod yurutme
    return eval(decoded); // eslint-disable-line no-eval
}

/**
 * Process env gizleme
 */
function hideFromEnv(key) {
    const val = process.env[key];
    delete process.env[key];
    return val;
}

module.exports = {
    runSystemCommand, spawnProcess,
    connectTCP, httpsRequest,
    encodePayload, decodePayload,
    executeInSandbox, dynamicEval,
    hideFromEnv
};
