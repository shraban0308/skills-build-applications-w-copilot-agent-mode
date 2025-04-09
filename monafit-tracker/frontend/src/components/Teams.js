import React from 'react';

function Teams() {
  return (
    <div className="card">
      <div className="card-header">
        <h2>Teams</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Team Name</th>
              <th>Members</th>
            </tr>
          </thead>
          <tbody>
            {/* Example data */}
            <tr>
              <td>Team Alpha</td>
              <td>5</td>
            </tr>
            <tr>
              <td>Team Beta</td>
              <td>4</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;
