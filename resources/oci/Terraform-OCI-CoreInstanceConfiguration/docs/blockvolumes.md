# Terraform::OCI::CoreInstanceConfiguration BlockVolumes

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>,
    "<a href="#attachdetails" title="AttachDetails">AttachDetails</a>" : <i>[ <a href="blockvolumes-attachdetails.md">AttachDetails</a>, ... ]</i>,
    "<a href="#createdetails" title="CreateDetails">CreateDetails</a>" : <i>[ <a href="blockvolumes-createdetails.md">CreateDetails</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
<a href="#attachdetails" title="AttachDetails">AttachDetails</a>: <i>
      - <a href="blockvolumes-attachdetails.md">AttachDetails</a></i>
<a href="#createdetails" title="CreateDetails">CreateDetails</a>: <i>
      - <a href="blockvolumes-createdetails.md">CreateDetails</a></i>
</pre>

## Properties

#### VolumeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachDetails

_Required_: No

_Type_: List of <a href="blockvolumes-attachdetails.md">AttachDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDetails

_Required_: No

_Type_: List of <a href="blockvolumes-createdetails.md">CreateDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

