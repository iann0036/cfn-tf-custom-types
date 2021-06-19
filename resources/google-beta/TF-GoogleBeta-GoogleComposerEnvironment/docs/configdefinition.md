# TF::GoogleBeta::GoogleComposerEnvironment ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
    "<a href="#databaseconfig" title="DatabaseConfig">DatabaseConfig</a>" : <i>[ <a href="databaseconfigdefinition.md">DatabaseConfigDefinition</a>, ... ]</i>,
    "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ <a href="encryptionconfigdefinition.md">EncryptionConfigDefinition</a>, ... ]</i>,
    "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
    "<a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>" : <i>[ <a href="privateenvironmentconfigdefinition.md">PrivateEnvironmentConfigDefinition</a>, ... ]</i>,
    "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a>, ... ]</i>,
    "<a href="#webserverconfig" title="WebServerConfig">WebServerConfig</a>" : <i>[ <a href="webserverconfigdefinition.md">WebServerConfigDefinition</a>, ... ]</i>,
    "<a href="#webservernetworkaccesscontrol" title="WebServerNetworkAccessControl">WebServerNetworkAccessControl</a>" : <i>[ <a href="webservernetworkaccesscontroldefinition.md">WebServerNetworkAccessControlDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
<a href="#databaseconfig" title="DatabaseConfig">DatabaseConfig</a>: <i>
      - <a href="databaseconfigdefinition.md">DatabaseConfigDefinition</a></i>
<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>: <i>
      - <a href="encryptionconfigdefinition.md">EncryptionConfigDefinition</a></i>
<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfigdefinition.md">NodeConfigDefinition</a></i>
<a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>: <i>
      - <a href="privateenvironmentconfigdefinition.md">PrivateEnvironmentConfigDefinition</a></i>
<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a></i>
<a href="#webserverconfig" title="WebServerConfig">WebServerConfig</a>: <i>
      - <a href="webserverconfigdefinition.md">WebServerConfigDefinition</a></i>
<a href="#webservernetworkaccesscontrol" title="WebServerNetworkAccessControl">WebServerNetworkAccessControl</a>: <i>
      - <a href="webservernetworkaccesscontroldefinition.md">WebServerNetworkAccessControlDefinition</a></i>
</pre>

## Properties

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseConfig

_Required_: No

_Type_: List of <a href="databaseconfigdefinition.md">DatabaseConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfig

_Required_: No

_Type_: List of <a href="encryptionconfigdefinition.md">EncryptionConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEnvironmentConfig

_Required_: No

_Type_: List of <a href="privateenvironmentconfigdefinition.md">PrivateEnvironmentConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No

_Type_: List of <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebServerConfig

_Required_: No

_Type_: List of <a href="webserverconfigdefinition.md">WebServerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebServerNetworkAccessControl

_Required_: No

_Type_: List of <a href="webservernetworkaccesscontroldefinition.md">WebServerNetworkAccessControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

