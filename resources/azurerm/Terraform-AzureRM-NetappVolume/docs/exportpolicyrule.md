# Terraform::AzureRM::NetappVolume ExportPolicyRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedclients" title="AllowedClients">AllowedClients</a>" : <i>[ String, ... ]</i>,
    "<a href="#cifsenabled" title="CifsEnabled">CifsEnabled</a>" : <i>Boolean</i>,
    "<a href="#nfsv3enabled" title="Nfsv3Enabled">Nfsv3Enabled</a>" : <i>Boolean</i>,
    "<a href="#nfsv4enabled" title="Nfsv4Enabled">Nfsv4Enabled</a>" : <i>Boolean</i>,
    "<a href="#protocolsenabled" title="ProtocolsEnabled">ProtocolsEnabled</a>" : <i>[ String, ... ]</i>,
    "<a href="#ruleindex" title="RuleIndex">RuleIndex</a>" : <i>Double</i>,
    "<a href="#unixreadonly" title="UnixReadOnly">UnixReadOnly</a>" : <i>Boolean</i>,
    "<a href="#unixreadwrite" title="UnixReadWrite">UnixReadWrite</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#allowedclients" title="AllowedClients">AllowedClients</a>: <i>
      - String</i>
<a href="#cifsenabled" title="CifsEnabled">CifsEnabled</a>: <i>Boolean</i>
<a href="#nfsv3enabled" title="Nfsv3Enabled">Nfsv3Enabled</a>: <i>Boolean</i>
<a href="#nfsv4enabled" title="Nfsv4Enabled">Nfsv4Enabled</a>: <i>Boolean</i>
<a href="#protocolsenabled" title="ProtocolsEnabled">ProtocolsEnabled</a>: <i>
      - String</i>
<a href="#ruleindex" title="RuleIndex">RuleIndex</a>: <i>Double</i>
<a href="#unixreadonly" title="UnixReadOnly">UnixReadOnly</a>: <i>Boolean</i>
<a href="#unixreadwrite" title="UnixReadWrite">UnixReadWrite</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowedClients

A list of allowed clients IPv4 addresses.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CifsEnabled

Is the CIFS protocol allowed?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfsv3Enabled

Is the NFSv3 protocol allowed?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfsv4Enabled

Is the NFSv4 protocol allowed?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolsEnabled

A list of allowed protocols. Valid values include `CIFS`, `NFSv3`, or `NFSv4.1`. Only one value is supported at this time. This replaces the previous arguments: `cifs_enabled`, `nfsv3_enabled` and `nfsv4_enabled`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleIndex

The index number of the rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnixReadOnly

Is the file system on unix read only?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnixReadWrite

Is the file system on unix read and write?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

