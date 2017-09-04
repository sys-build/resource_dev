#!/bin/bash

QEMU_AARCH64=~/sda6/bin/qemu/qemu-2.10.0/bin/qemu-system-aarch64

${QEMU_AARCH64} -machine virt -cpu cortex-a57 -machine type=virt -nographic -smp 1 -m 2048 \
-kernel ../out/arch/arm64/boot/Image --append "console=ttyAMA0" -fsdev local,id=r,path=../,security_model=none \
-device virtio-9p-device,fsdev=r,mount_tag=r
