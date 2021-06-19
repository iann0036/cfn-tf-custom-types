# TF::Rancher2::ClusterTemplate EtcdDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cacert" title="CaCert">CaCert</a>" : <i>String</i>,
    "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
    "<a href="#creation" title="Creation">Creation</a>" : <i>String</i>,
    "<a href="#externalurls" title="ExternalUrls">ExternalUrls</a>" : <i>[ String, ... ]</i>,
    "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ <a href="extraargsdefinition.md">ExtraArgsDefinition</a>, ... ]</i>,
    "<a href="#extrabinds" title="ExtraBinds">ExtraBinds</a>" : <i>[ String, ... ]</i>,
    "<a href="#extraenv" title="ExtraEnv">ExtraEnv</a>" : <i>[ String, ... ]</i>,
    "<a href="#gid" title="Gid">Gid</a>" : <i>Double</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#retention" title="Retention">Retention</a>" : <i>String</i>,
    "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>Boolean</i>,
    "<a href="#uid" title="Uid">Uid</a>" : <i>Double</i>,
    "<a href="#backupconfig" title="BackupConfig">BackupConfig</a>" : <i>[ <a href="backupconfigdefinition.md">BackupConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cacert" title="CaCert">CaCert</a>: <i>String</i>
<a href="#cert" title="Cert">Cert</a>: <i>String</i>
<a href="#creation" title="Creation">Creation</a>: <i>String</i>
<a href="#externalurls" title="ExternalUrls">ExternalUrls</a>: <i>
      - String</i>
<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - <a href="extraargsdefinition.md">ExtraArgsDefinition</a></i>
<a href="#extrabinds" title="ExtraBinds">ExtraBinds</a>: <i>
      - String</i>
<a href="#extraenv" title="ExtraEnv">ExtraEnv</a>: <i>
      - String</i>
<a href="#gid" title="Gid">Gid</a>: <i>Double</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#retention" title="Retention">Retention</a>: <i>String</i>
<a href="#snapshot" title="Snapshot">Snapshot</a>: <i>Boolean</i>
<a href="#uid" title="Uid">Uid</a>: <i>Double</i>
<a href="#backupconfig" title="BackupConfig">BackupConfig</a>: <i>
      - <a href="backupconfigdefinition.md">BackupConfigDefinition</a></i>
</pre>

## Properties

#### CaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Creation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraArgs

_Required_: No

_Type_: List of <a href="extraargsdefinition.md">ExtraArgsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraBinds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraEnv

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retention

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfig

_Required_: No

_Type_: List of <a href="backupconfigdefinition.md">BackupConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

