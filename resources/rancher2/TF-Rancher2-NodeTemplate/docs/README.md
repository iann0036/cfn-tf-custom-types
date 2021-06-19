# TF::Rancher2::NodeTemplate

CloudFormation equivalent of rancher2_node_template

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::NodeTemplate",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#authcertificateauthority" title="AuthCertificateAuthority">AuthCertificateAuthority</a>" : <i>String</i>,
        "<a href="#authkey" title="AuthKey">AuthKey</a>" : <i>String</i>,
        "<a href="#cloudcredentialid" title="CloudCredentialId">CloudCredentialId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#driverid" title="DriverId">DriverId</a>" : <i>String</i>,
        "<a href="#engineenv" title="EngineEnv">EngineEnv</a>" : <i>[ <a href="engineenvdefinition.md">EngineEnvDefinition</a>, ... ]</i>,
        "<a href="#engineinsecureregistry" title="EngineInsecureRegistry">EngineInsecureRegistry</a>" : <i>[ String, ... ]</i>,
        "<a href="#engineinstallurl" title="EngineInstallUrl">EngineInstallUrl</a>" : <i>String</i>,
        "<a href="#enginelabel" title="EngineLabel">EngineLabel</a>" : <i>[ <a href="enginelabeldefinition.md">EngineLabelDefinition</a>, ... ]</i>,
        "<a href="#engineopt" title="EngineOpt">EngineOpt</a>" : <i>[ <a href="engineoptdefinition.md">EngineOptDefinition</a>, ... ]</i>,
        "<a href="#engineregistrymirror" title="EngineRegistryMirror">EngineRegistryMirror</a>" : <i>[ String, ... ]</i>,
        "<a href="#enginestoragedriver" title="EngineStorageDriver">EngineStorageDriver</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#useinternalipaddress" title="UseInternalIpAddress">UseInternalIpAddress</a>" : <i>Boolean</i>,
        "<a href="#amazonec2config" title="Amazonec2Config">Amazonec2Config</a>" : <i>[ <a href="amazonec2configdefinition.md">Amazonec2ConfigDefinition</a>, ... ]</i>,
        "<a href="#azureconfig" title="AzureConfig">AzureConfig</a>" : <i>[ <a href="azureconfigdefinition.md">AzureConfigDefinition</a>, ... ]</i>,
        "<a href="#digitaloceanconfig" title="DigitaloceanConfig">DigitaloceanConfig</a>" : <i>[ <a href="digitaloceanconfigdefinition.md">DigitaloceanConfigDefinition</a>, ... ]</i>,
        "<a href="#hetznerconfig" title="HetznerConfig">HetznerConfig</a>" : <i>[ <a href="hetznerconfigdefinition.md">HetznerConfigDefinition</a>, ... ]</i>,
        "<a href="#linodeconfig" title="LinodeConfig">LinodeConfig</a>" : <i>[ <a href="linodeconfigdefinition.md">LinodeConfigDefinition</a>, ... ]</i>,
        "<a href="#nodetaints" title="NodeTaints">NodeTaints</a>" : <i>[ <a href="nodetaintsdefinition.md">NodeTaintsDefinition</a>, ... ]</i>,
        "<a href="#opennebulaconfig" title="OpennebulaConfig">OpennebulaConfig</a>" : <i>[ <a href="opennebulaconfigdefinition.md">OpennebulaConfigDefinition</a>, ... ]</i>,
        "<a href="#openstackconfig" title="OpenstackConfig">OpenstackConfig</a>" : <i>[ <a href="openstackconfigdefinition.md">OpenstackConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vsphereconfig" title="VsphereConfig">VsphereConfig</a>" : <i>[ <a href="vsphereconfigdefinition.md">VsphereConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::NodeTemplate
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#authcertificateauthority" title="AuthCertificateAuthority">AuthCertificateAuthority</a>: <i>String</i>
    <a href="#authkey" title="AuthKey">AuthKey</a>: <i>String</i>
    <a href="#cloudcredentialid" title="CloudCredentialId">CloudCredentialId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#driverid" title="DriverId">DriverId</a>: <i>String</i>
    <a href="#engineenv" title="EngineEnv">EngineEnv</a>: <i>
      - <a href="engineenvdefinition.md">EngineEnvDefinition</a></i>
    <a href="#engineinsecureregistry" title="EngineInsecureRegistry">EngineInsecureRegistry</a>: <i>
      - String</i>
    <a href="#engineinstallurl" title="EngineInstallUrl">EngineInstallUrl</a>: <i>String</i>
    <a href="#enginelabel" title="EngineLabel">EngineLabel</a>: <i>
      - <a href="enginelabeldefinition.md">EngineLabelDefinition</a></i>
    <a href="#engineopt" title="EngineOpt">EngineOpt</a>: <i>
      - <a href="engineoptdefinition.md">EngineOptDefinition</a></i>
    <a href="#engineregistrymirror" title="EngineRegistryMirror">EngineRegistryMirror</a>: <i>
      - String</i>
    <a href="#enginestoragedriver" title="EngineStorageDriver">EngineStorageDriver</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#useinternalipaddress" title="UseInternalIpAddress">UseInternalIpAddress</a>: <i>Boolean</i>
    <a href="#amazonec2config" title="Amazonec2Config">Amazonec2Config</a>: <i>
      - <a href="amazonec2configdefinition.md">Amazonec2ConfigDefinition</a></i>
    <a href="#azureconfig" title="AzureConfig">AzureConfig</a>: <i>
      - <a href="azureconfigdefinition.md">AzureConfigDefinition</a></i>
    <a href="#digitaloceanconfig" title="DigitaloceanConfig">DigitaloceanConfig</a>: <i>
      - <a href="digitaloceanconfigdefinition.md">DigitaloceanConfigDefinition</a></i>
    <a href="#hetznerconfig" title="HetznerConfig">HetznerConfig</a>: <i>
      - <a href="hetznerconfigdefinition.md">HetznerConfigDefinition</a></i>
    <a href="#linodeconfig" title="LinodeConfig">LinodeConfig</a>: <i>
      - <a href="linodeconfigdefinition.md">LinodeConfigDefinition</a></i>
    <a href="#nodetaints" title="NodeTaints">NodeTaints</a>: <i>
      - <a href="nodetaintsdefinition.md">NodeTaintsDefinition</a></i>
    <a href="#opennebulaconfig" title="OpennebulaConfig">OpennebulaConfig</a>: <i>
      - <a href="opennebulaconfigdefinition.md">OpennebulaConfigDefinition</a></i>
    <a href="#openstackconfig" title="OpenstackConfig">OpenstackConfig</a>: <i>
      - <a href="openstackconfigdefinition.md">OpenstackConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vsphereconfig" title="VsphereConfig">VsphereConfig</a>: <i>
      - <a href="vsphereconfigdefinition.md">VsphereConfigDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCertificateAuthority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudCredentialId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineEnv

_Required_: No

_Type_: List of <a href="engineenvdefinition.md">EngineEnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineInsecureRegistry

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineInstallUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineLabel

_Required_: No

_Type_: List of <a href="enginelabeldefinition.md">EngineLabelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineOpt

_Required_: No

_Type_: List of <a href="engineoptdefinition.md">EngineOptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineRegistryMirror

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineStorageDriver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseInternalIpAddress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Amazonec2Config

_Required_: No

_Type_: List of <a href="amazonec2configdefinition.md">Amazonec2ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureConfig

_Required_: No

_Type_: List of <a href="azureconfigdefinition.md">AzureConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DigitaloceanConfig

_Required_: No

_Type_: List of <a href="digitaloceanconfigdefinition.md">DigitaloceanConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HetznerConfig

_Required_: No

_Type_: List of <a href="hetznerconfigdefinition.md">HetznerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinodeConfig

_Required_: No

_Type_: List of <a href="linodeconfigdefinition.md">LinodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeTaints

_Required_: No

_Type_: List of <a href="nodetaintsdefinition.md">NodeTaintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpennebulaConfig

_Required_: No

_Type_: List of <a href="opennebulaconfigdefinition.md">OpennebulaConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackConfig

_Required_: No

_Type_: List of <a href="openstackconfigdefinition.md">OpenstackConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereConfig

_Required_: No

_Type_: List of <a href="vsphereconfigdefinition.md">VsphereConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Driver

Returns the <code>Driver</code> value.

#### Id

Returns the <code>Id</code> value.

