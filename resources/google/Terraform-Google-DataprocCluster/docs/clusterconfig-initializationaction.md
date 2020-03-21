# Terraform::Google::DataprocCluster ClusterConfig InitializationAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#script" title="Script">Script</a>" : <i>String</i>,
    "<a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#script" title="Script">Script</a>: <i>String</i>
<a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>: <i>Double</i>
</pre>

## Properties

#### Script

The script to be executed during initialization of the cluster.
The script must be a GCS file with a gs:// prefix.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSec

The maximum duration (in seconds) which `script` is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

