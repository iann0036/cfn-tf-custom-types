# Terraform::Alicloud::ImageImport

Import a copy of your local on-premise file to ECS, and appear as a custom replacement in the corresponding domain.

-> **NOTE:** You must upload the image file to the object storage OSS in advance.

-> **NOTE:** The region where the image is imported must be the same region as the OSS bucket where the image file is uploaded.

-> **NOTE:** Available in 1.69.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::ImageImport",
    "Properties" : {
        "<a href="#architecture" title="Architecture">Architecture</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>String</i>,
        "<a href="#diskdevicemapping" title="DiskDeviceMapping">DiskDeviceMapping</a>" : <i>[ <a href="diskdevicemapping.md">DiskDeviceMapping</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::ImageImport
Properties:
    <a href="#architecture" title="Architecture">Architecture</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#platform" title="Platform">Platform</a>: <i>String</i>
    <a href="#diskdevicemapping" title="DiskDeviceMapping">DiskDeviceMapping</a>: <i>
      - <a href="diskdevicemapping.md">DiskDeviceMapping</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Architecture

(Optional, ForceNew) Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `i386` , Default is `x86_64`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Optional) Description of the image. The length is 2 to 256 English or Chinese characters, and cannot begin with http: // and https: //.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

(Optional) The image name. The length is 2 ~ 128 English or Chinese characters. Must start with a capital letter or Chinese, and cannot start with http: // and https: //. Can contain numbers, colons (:), underscores (_), or hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

(Optional, ForceNew).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

(Optional, ForceNew) Operating system platform type. Valid values: `windows`, Default is `linux`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

(Optional, ForceNew) Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `CentOS`, `Ubuntu`, `SUSE`, `OpenSUSE`, `Debian`, `CoreOS`, `Windows Server 2003`, `Windows Server 2008`, `Windows Server 2012`, `Windows 7`, Default is `Others Linux`, `Customized Linux`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskDeviceMapping

_Required_: No

_Type_: List of <a href="diskdevicemapping.md">DiskDeviceMapping</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

