# Tailscale + SSH from iPhone

## 1. Install Tailscale on iPhone

1. Open the **App Store** and search for "Tailscale"
2. Install and open Tailscale
3. Tap **Sign in** — use the same account you used on your Mac
4. When prompted, allow the VPN configuration
5. Toggle Tailscale **ON**

## 2. Verify both devices are connected

1. In the Tailscale app on your phone, you should see your Mac listed (e.g. "jonathans-macbook-pro")
2. You can also check at https://login.tailscale.com/admin/machines
3. Both devices should show as "Connected"

## 3. Install a terminal app

**Blink Shell** (recommended, paid)
- Full tmux support, great keyboard
- Mosh support for flaky connections

**Termius** (free tier works)
- Clean UI, easy key management
- Free tier supports basic SSH

## 4. Import your SSH key

You need to transfer your private key to your phone. The safest way:

### Option A: AirDrop
1. On your Mac, run: `open ~/.ssh/` in Finder
2. AirDrop `id_ed25519` (private key) to your iPhone
3. Open it in your terminal app to import

### Option B: Clipboard (quick but less secure)
1. On Mac: `cat ~/.ssh/id_ed25519 | pbcopy`
2. Use Universal Clipboard (both devices signed into same iCloud) to paste into your terminal app's key import

### Option C: QR code
1. On Mac: `qrencode -t ansiutf8 < ~/.ssh/id_ed25519` (install via `brew install qrencode`)
2. Scan with phone camera

## 5. Configure the SSH connection

- **Hostname**: $TAILSCALE_IP (see .env)
- **Username**: $MAC_USER (see .env)
- **Port**: 22
- **Auth**: The private key you imported

## 6. Test the connection

In your terminal app, run:
```
ssh $MAC_USER (see .env)@$TAILSCALE_IP (see .env)
```

You should get a shell on your Mac. Then try:
```
tmux ls
tmux attach -t ccgram
```
