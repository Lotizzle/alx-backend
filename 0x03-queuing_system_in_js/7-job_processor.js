// 7-job_processor.js

import kue from  'kue';

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Sends a notification.
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to send.
 * @param {object} job - The job object.
 * @param {function} done - The callback function.
 */
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100); // Track progress of 0 out of 100

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100); // Track progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
