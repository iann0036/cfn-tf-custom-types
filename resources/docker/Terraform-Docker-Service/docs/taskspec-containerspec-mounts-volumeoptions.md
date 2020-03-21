# Terraform::Docker::Service TaskSpec ContainerSpec Mounts VolumeOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#drivername" title="DriverName">DriverName</a>" : <i>String</i>,
    "<a href="#driveroptions" title="DriverOptions">DriverOptions</a>" : <i>[ <a href="taskspec-containerspec-mounts-volumeoptions-driveroptions.md">DriverOptions</a>, ... ]</i>,
    "<a href="#nocopy" title="NoCopy">NoCopy</a>" : <i>Boolean</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="taskspec-containerspec-mounts-volumeoptions-labels.md">Labels</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#drivername" title="DriverName">DriverName</a>: <i>String</i>
<a href="#driveroptions" title="DriverOptions">DriverOptions</a>: <i>
      - <a href="taskspec-containerspec-mounts-volumeoptions-driveroptions.md">DriverOptions</a></i>
<a href="#nocopy" title="NoCopy">NoCopy</a>: <i>Boolean</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="taskspec-containerspec-mounts-volumeoptions-labels.md">Labels</a></i>
</pre>

## Properties

#### DriverName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverOptions

_Required_: No

_Type_: List of <a href="taskspec-containerspec-mounts-volumeoptions-driveroptions.md">DriverOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoCopy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="taskspec-containerspec-mounts-volumeoptions-labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

