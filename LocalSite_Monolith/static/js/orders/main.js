import { isTgWebApp } from '../checkApp.js';
import { initializeOnContentLoaded } from './contentLoaded.js';

document.addEventListener('DOMContentLoaded', function() {
    if (!isTgWebApp()) {
        return;
    }

    initializeOnContentLoaded();
});