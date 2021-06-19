# TF::ECL::ImagestoragesImageV2

Manages a V2 image resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::ImagestoragesImageV2",
    "Properties" : {
        "<a href="#containerformat" title="ContainerFormat">ContainerFormat</a>" : <i>String</i>,
        "<a href="#diskformat" title="DiskFormat">DiskFormat</a>" : <i>String</i>,
        "<a href="#licenseswitch" title="LicenseSwitch">LicenseSwitch</a>" : <i>String</i>,
        "<a href="#localfilepath" title="LocalFilePath">LocalFilePath</a>" : <i>String</i>,
        "<a href="#mindiskgb" title="MinDiskGb">MinDiskGb</a>" : <i>Double</i>,
        "<a href="#minrammb" title="MinRamMb">MinRamMb</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
        "<a href="#protected" title="Protected">Protected</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#verifychecksum" title="VerifyChecksum">VerifyChecksum</a>" : <i>Boolean</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::ImagestoragesImageV2
Properties:
    <a href="#containerformat" title="ContainerFormat">ContainerFormat</a>: <i>String</i>
    <a href="#diskformat" title="DiskFormat">DiskFormat</a>: <i>String</i>
    <a href="#licenseswitch" title="LicenseSwitch">LicenseSwitch</a>: <i>String</i>
    <a href="#localfilepath" title="LocalFilePath">LocalFilePath</a>: <i>String</i>
    <a href="#mindiskgb" title="MinDiskGb">MinDiskGb</a>: <i>Double</i>
    <a href="#minrammb" title="MinRamMb">MinRamMb</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
    <a href="#protected" title="Protected">Protected</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#verifychecksum" title="VerifyChecksum">VerifyChecksum</a>: <i>Boolean</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ContainerFormat

Format of the container. Must be "bare".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskFormat

Format of the disk. Must be one of "raw", "qcow2", "iso".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseSwitch

Switch destination of the license type. Must be one of "WindowsServer_2012R2_Standard_64bit_ComLicense", "WindowsServer_2012_Standard_64bit_ComLicense", "WindowsServer_2008R2_Enterprise_64bit_ComLicense", "WindowsServer_2008R2_Standard_64bit_ComLicense", "WindowsServer_2008_Enterprise_64bit_ComLicense", "WindowsServer_2008_Standard_64bit_ComLicense", "Red_Hat_Enterprise_Linux_6_64bit_BYOL".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalFilePath

This is the filepath of the raw image file that will be uploaded to Glance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinDiskGb

Amount of disk space (in GB) required to boot image. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRamMb

Amount of ram (in MB) required to boot image. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Descriptive name for the image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protected

If true, image will not be deletable. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Imagestorage client.
Images are associated with accounts, but a Imagestroage client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

String related to the image.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyChecksum

If false, the checksum will not be verified once the image is finished uploading. Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

Scope of image accessibility. Must be one of "public", "private". Defaults to "private".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Checksum

Returns the <code>Checksum</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### File

Returns the <code>File</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### Schema

Returns the <code>Schema</code> value.

#### SizeBytes

Returns the <code>SizeBytes</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdateAt

Returns the <code>UpdateAt</code> value.

