from wakeonlan import send_magic_packet
from sensitive import NAS_MAC_ADDRESS

send_magic_packet(NAS_MAC_ADDRESS)
