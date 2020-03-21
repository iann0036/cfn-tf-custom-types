# Terraform::FlexibleEngine::RdsInstanceV1 Ha

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#replicationmode" title="Replicationmode">Replicationmode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#replicationmode" title="Replicationmode">Replicationmode</a>: <i>String</i>
</pre>

## Properties

#### Enable

Specifies the configured parameters on the HA.
Valid value: The value is true or false. The value true indicates creating
HA DB instances. The value false indicates creating a single DB instance.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replicationmode

Specifies the replication mode for the standby DB instance.
The value cannot be empty.
For MySQL, the value is async or semisync.
For PostgreSQL, the value is async or sync.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

