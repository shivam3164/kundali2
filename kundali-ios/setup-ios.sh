#!/bin/bash

echo "Setting up iOS development environment..."

# Check if Xcode is installed
if [ ! -d "/Applications/Xcode.app" ]; then
    echo "Error: Xcode is not installed. Please install from the App Store."
    exit 1
fi

# Accept Xcode license
echo "Accepting Xcode license..."
sudo xcodebuild -license accept 2>/dev/null || true

# Set Xcode path
echo "Setting Xcode path..."
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer

# Install iOS Simulator runtime if needed
echo "Checking iOS Simulator..."
xcrun simctl list devices 2>/dev/null | head -5

# Install CocoaPods if not present
if ! command -v pod &> /dev/null; then
    echo "Installing CocoaPods..."
    sudo gem install cocoapods
fi

# Create native iOS project
echo "Creating native iOS project..."
cd /Users/shivam/Documents/GenAI/kundali/kundali-ios
npx expo prebuild --platform ios --clean

# Install iOS dependencies
echo "Installing iOS dependencies..."
cd ios && pod install && cd ..

echo ""
echo "Setup complete! Run the app with:"
echo "  npx expo run:ios"
echo ""
echo "Or start the dev server and press 'i' for iOS:"
echo "  npx expo start"
