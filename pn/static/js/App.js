/* eslint-env browser */
import 'regenerator-runtime/runtime';

// Forces the evaluation of bootstrap plugins in the global context.
import 'bootstrap.native/dist/bootstrap-native-v4';

import controllers from './controllers';
import DOMRouter from './core/DOMRouter';


// Defines the router and initializes it!
const router = new DOMRouter(controllers);
document.addEventListener('DOMContentLoaded', () => {
  router.init();
});
