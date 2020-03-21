# Terraform::HCloud::Volume

Provides a Hetzner Cloud volume resource to manage volumes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HCloud::Volume",
    "Properties" : {
        "<a href="#automount" title="Automount">Automount</a>" : <i>Boolean</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>Double</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HCloud::Volume
Properties:
    <a href="#automount" title="Automount">Automount</a>: <i>Boolean</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>Double</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
</pre>

## Properties

#### Automount

Automount the volume upon attaching it (server_id must be provided).
- `format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Format volume after creation. `xfs` or `ext4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Location of the volume to create, optional if server_id argument is passed.
- `automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the volume to create (must be unique per project).
- `size` - (Required, int) Size of the volume (in GB).
- `server` - (Optional, int) Server to attach the Volume to, optional if location argument is passed.
- `location` - (Optional, string) Location of the volume to create, optional if server_id argument is passed.
- `automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Size of the volume (in GB).
- `server` - (Optional, int) Server to attach the Volume to, optional if location argument is passed.
- `location` - (Optional, string) Location of the volume to create, optional if server_id argument is passed.
- `automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### LinuxDevice

Returns the <code>LinuxDevice</code> value.

