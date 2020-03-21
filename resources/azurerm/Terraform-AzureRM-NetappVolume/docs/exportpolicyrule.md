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

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CifsEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfsv3Enabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfsv4Enabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolsEnabled

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleIndex

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnixReadOnly

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnixReadWrite

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

