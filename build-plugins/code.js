const { widget } = figma;
const { AutoLayout, Text, Image, Input, useEffect, useSyncedState } = widget;

const BACKEND_URL = 'https://rbg-mindsparks.hallaw.com/remove-background';

async function runBackgroundRemover(file) {
    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch(BACKEND_URL, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        if (data.image) {
            return data.image;
        } else {
            throw new Error('Failed to process the image');
        }
    } catch (error) {
        console.error(error);
        return null;
    }
}

widget.register(() => {
    const [image, setImage] = useSyncedState('image', null);
    const [fileName, setFileName] = useSyncedState('fileName', '');

    async function handleFileInput(event) {
        const file = event.target.files[0];
        if (!file) {
            figma.notify('Please select an image file!');
            return;
        }

        setFileName(file.name);
        const base64Image = await runBackgroundRemover(file);
        if (base64Image) {
            setImage(base64Image);
        } else {
            figma.notify('Failed to remove background!');
        }
    }

    return (
        AutoLayout({
            direction: 'vertical',
            padding: 16,
            spacing: 12,
            children: [
                Text({ value: 'Background Remover' }),
                Input({
                    placeholder: 'Select an image',
                    type: 'file',
                    onChange: handleFileInput,
                }),
                fileName && Text({ value: `Selected File: ${fileName}` }),
                image && Image({ src: `data:image/png;base64,${image}` }),
            ],
        })
    );
});