# Samba (SMB) Setup

## 1. Create a NAS directory

Use the existing SD card as storage (v1, for learning and light use):

```bash
mkdir -p /home/your-username/nas-share
chmod 700 /home/your-username/nas-share
```
---

## 2. Install Samba

```bash
sudo apt install -y samba samba-common-bin
```

---

## 3. Configure the share

Edit `/etc/samba/smb.conf`:

```bash
sudo nano /etc/samba/smb.conf
```

Add at the end:

[nas]
`
path = /home/your-username/nas-share
browseable = yes
read only = no
valid users = your-username
create mask = 0660
directory mask = 0770
`

Save and exit.

---

## 4. Set Samba password and restart

```bash
sudo smbpasswd -a your-username
sudo systemctl restart smbd
```

---

## 5. Test locally from the Pi

Make sure you can read/write inside the share directory:

```bash
touch /home/your-username/nas-share/testfile.txt
```
```bash
ls -l /home/your-username/nas-share
```

You can now access the share from a Linux client using:

```bash
sudo mkdir -p /mnt/pinas
sudo mount -t cifs //192.168.x.x/nas /mnt/pinas -o username=your-username
```

Replace `192.168.x.x` with your Pi’s LAN IP