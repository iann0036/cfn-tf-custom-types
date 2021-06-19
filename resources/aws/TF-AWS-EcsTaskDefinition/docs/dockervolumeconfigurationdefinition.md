# TF::AWS::EcsTaskDefinition DockerVolumeConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoprovision" title="Autoprovision">Autoprovision</a>" : <i>Boolean</i>,
    "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
    "<a href="#driveropts" title="DriverOpts">DriverOpts</a>" : <i>[ <a href="driveroptsdefinition.md">DriverOptsDefinition</a>, ... ]</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autoprovision" title="Autoprovision">Autoprovision</a>: <i>Boolean</i>
<a href="#driver" title="Driver">Driver</a>: <i>String</i>
<a href="#driveropts" title="DriverOpts">DriverOpts</a>: <i>
      - <a href="driveroptsdefinition.md">DriverOptsDefinition</a></i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
</pre>

## Properties

#### Autoprovision

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Driver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverOpts

_Required_: No

_Type_: List of <a href="driveroptsdefinition.md">DriverOptsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

