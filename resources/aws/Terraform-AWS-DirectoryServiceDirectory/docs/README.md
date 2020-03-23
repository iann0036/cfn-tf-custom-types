# Terraform::AWS::DirectoryServiceDirectory

Provides a Simple or Managed Microsoft directory in AWS Directory Service.

~> **Note:** All arguments including the password and customer username will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DirectoryServiceDirectory",
    "Properties" : {
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#edition" title="Edition">Edition</a>" : <i>String</i>,
        "<a href="#enablesso" title="EnableSso">EnableSso</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#shortname" title="ShortName">ShortName</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#connectsettings" title="ConnectSettings">ConnectSettings</a>" : <i>[ <a href="connectsettings.md">ConnectSettings</a>, ... ]</i>,
        "<a href="#vpcsettings" title="VpcSettings">VpcSettings</a>" : <i>[ <a href="vpcsettings.md">VpcSettings</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DirectoryServiceDirectory
Properties:
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#edition" title="Edition">Edition</a>: <i>String</i>
    <a href="#enablesso" title="EnableSso">EnableSso</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#shortname" title="ShortName">ShortName</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#connectsettings" title="ConnectSettings">ConnectSettings</a>: <i>
      - <a href="connectsettings.md">ConnectSettings</a></i>
    <a href="#vpcsettings" title="VpcSettings">VpcSettings</a>: <i>
      - <a href="vpcsettings.md">VpcSettings</a></i>
</pre>

## Properties

#### Alias

The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A textual description for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Edition

The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSso

Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The fully qualified name for the directory, such as `corp.example.com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password for the directory administrator or connector user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortName

The short name of the directory, such as `CORP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the directory (`Small` or `Large` are accepted values).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectSettings

_Required_: No

_Type_: List of <a href="connectsettings.md">ConnectSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSettings

_Required_: No

_Type_: List of <a href="vpcsettings.md">VpcSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessUrl

Returns the <code>AccessUrl</code> value.

#### DnsIpAddresses

Returns the <code>DnsIpAddresses</code> value.

#### Id

Returns the <code>Id</code> value.

#### SecurityGroupId

Returns the <code>SecurityGroupId</code> value.

