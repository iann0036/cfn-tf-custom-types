# TF::ProfitBricks::Server VolumeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
    "<a href="#bus" title="Bus">Bus</a>" : <i>String</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
    "<a href="#imagepassword" title="ImagePassword">ImagePassword</a>" : <i>String</i>,
    "<a href="#licencetype" title="LicenceType">LicenceType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
<a href="#bus" title="Bus">Bus</a>: <i>String</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
<a href="#imagepassword" title="ImagePassword">ImagePassword</a>: <i>String</i>
<a href="#licencetype" title="LicenceType">LicenceType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#sshkeypath" title="SshKeyPath">SshKeyPath</a>: <i>
      - String</i>
</pre>

## Properties

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyPath

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

