import React from 'react';

function Workouts() {
  return (
    <div className="card">
      <div className="card-header">
        <h2>Workouts</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Workout Name</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {/* Example data */}
            <tr>
              <td>Running</td>
              <td>Cardio exercise</td>
            </tr>
            <tr>
              <td>Swimming</td>
              <td>Full-body workout</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
