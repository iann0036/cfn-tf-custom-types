# TF::Tfe::TeamAccess PermissionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#runs" title="Runs">Runs</a>" : <i>String</i>,
    "<a href="#sentinelmocks" title="SentinelMocks">SentinelMocks</a>" : <i>String</i>,
    "<a href="#stateversions" title="StateVersions">StateVersions</a>" : <i>String</i>,
    "<a href="#variables" title="Variables">Variables</a>" : <i>String</i>,
    "<a href="#workspacelocking" title="WorkspaceLocking">WorkspaceLocking</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#runs" title="Runs">Runs</a>: <i>String</i>
<a href="#sentinelmocks" title="SentinelMocks">SentinelMocks</a>: <i>String</i>
<a href="#stateversions" title="StateVersions">StateVersions</a>: <i>String</i>
<a href="#variables" title="Variables">Variables</a>: <i>String</i>
<a href="#workspacelocking" title="WorkspaceLocking">WorkspaceLocking</a>: <i>Boolean</i>
</pre>

## Properties

#### Runs

The permission to grant the team on the workspace's runs. Valid values are `read`, `plan`, or `apply`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SentinelMocks

The permission to grant the team on the workspace's generated Sentinel mocks, Valid values are `none` or `read`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateVersions

The permission to grant the team on the workspace's state versions. Valid values are `none`, `read`, `read-outputs`, or `write`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variables

The permission to grant the team on the workspace's variables. Valid values are `none`, `read`, or `write`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceLocking

Boolean determining whether or not to grant the team permission to manually lock/unlock the workspace.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

