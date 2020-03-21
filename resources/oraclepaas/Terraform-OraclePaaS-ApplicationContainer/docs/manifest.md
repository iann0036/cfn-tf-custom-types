# Terraform::OraclePaaS::ApplicationContainer Manifest

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clustered" title="Clustered">Clustered</a>" : <i>Boolean</i>,
    "<a href="#command" title="Command">Command</a>" : <i>String</i>,
    "<a href="#healthcheckendpoint" title="HealthCheckEndpoint">HealthCheckEndpoint</a>" : <i>String</i>,
    "<a href="#home" title="Home">Home</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
    "<a href="#shutdowntime" title="ShutdownTime">ShutdownTime</a>" : <i>Double</i>,
    "<a href="#startuptime" title="StartupTime">StartupTime</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#release" title="Release">Release</a>" : <i>[ <a href="manifest-release.md">Release</a>, ... ]</i>,
    "<a href="#runtime" title="Runtime">Runtime</a>" : <i>[ <a href="manifest-runtime.md">Runtime</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clustered" title="Clustered">Clustered</a>: <i>Boolean</i>
<a href="#command" title="Command">Command</a>: <i>String</i>
<a href="#healthcheckendpoint" title="HealthCheckEndpoint">HealthCheckEndpoint</a>: <i>String</i>
<a href="#home" title="Home">Home</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#notes" title="Notes">Notes</a>: <i>String</i>
<a href="#shutdowntime" title="ShutdownTime">ShutdownTime</a>: <i>Double</i>
<a href="#startuptime" title="StartupTime">StartupTime</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#release" title="Release">Release</a>: <i>
      - <a href="manifest-release.md">Release</a></i>
<a href="#runtime" title="Runtime">Runtime</a>: <i>
      - <a href="manifest-runtime.md">Runtime</a></i>
</pre>

## Properties

#### Clustered

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckEndpoint

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Home

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownTime

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartupTime

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Release

_Required_: No
_Type_: List of <a href="manifest-release.md">Release</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: No
_Type_: List of <a href="manifest-runtime.md">Runtime</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

