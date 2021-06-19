# TF::AVI::Cloud DockerConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#appsyncfrequency" title="AppSyncFrequency">AppSyncFrequency</a>" : <i>Double</i>,
    "<a href="#catlskeyandcertificateref" title="CaTlsKeyAndCertificateRef">CaTlsKeyAndCertificateRef</a>" : <i>String</i>,
    "<a href="#clienttlskeyandcertificateref" title="ClientTlsKeyAndCertificateRef">ClientTlsKeyAndCertificateRef</a>" : <i>String</i>,
    "<a href="#containerportmatchhttpservice" title="ContainerPortMatchHttpService">ContainerPortMatchHttpService</a>" : <i>Boolean</i>,
    "<a href="#coredumpdirectory" title="CoredumpDirectory">CoredumpDirectory</a>" : <i>String</i>,
    "<a href="#disableautobackendservicesync" title="DisableAutoBackendServiceSync">DisableAutoBackendServiceSync</a>" : <i>Boolean</i>,
    "<a href="#disableautofrontendservicesync" title="DisableAutoFrontendServiceSync">DisableAutoFrontendServiceSync</a>" : <i>Boolean</i>,
    "<a href="#disableautosecreation" title="DisableAutoSeCreation">DisableAutoSeCreation</a>" : <i>Boolean</i>,
    "<a href="#enableeventsubscription" title="EnableEventSubscription">EnableEventSubscription</a>" : <i>Boolean</i>,
    "<a href="#feproxycontainerportasservice" title="FeproxyContainerPortAsService">FeproxyContainerPortAsService</a>" : <i>Boolean</i>,
    "<a href="#feproxyvipsenableproxyarp" title="FeproxyVipsEnableProxyArp">FeproxyVipsEnableProxyArp</a>" : <i>Boolean</i>,
    "<a href="#fleetendpoint" title="FleetEndpoint">FleetEndpoint</a>" : <i>String</i>,
    "<a href="#httpcontainerports" title="HttpContainerPorts">HttpContainerPorts</a>" : <i>[ Double, ... ]</i>,
    "<a href="#sedeploymentmethod" title="SeDeploymentMethod">SeDeploymentMethod</a>" : <i>String</i>,
    "<a href="#sespawnrate" title="SeSpawnRate">SeSpawnRate</a>" : <i>Double</i>,
    "<a href="#sevolume" title="SeVolume">SeVolume</a>" : <i>String</i>,
    "<a href="#servicesaccessibleallinterfaces" title="ServicesAccessibleAllInterfaces">ServicesAccessibleAllInterfaces</a>" : <i>Boolean</i>,
    "<a href="#sshuserref" title="SshUserRef">SshUserRef</a>" : <i>String</i>,
    "<a href="#ucpnodes" title="UcpNodes">UcpNodes</a>" : <i>[ String, ... ]</i>,
    "<a href="#usecontaineripport" title="UseContainerIpPort">UseContainerIpPort</a>" : <i>Boolean</i>,
    "<a href="#usecontrollerimage" title="UseControllerImage">UseControllerImage</a>" : <i>Boolean</i>,
    "<a href="#dockerregistryse" title="DockerRegistrySe">DockerRegistrySe</a>" : <i>[ <a href="dockerregistrysedefinition.md">DockerRegistrySeDefinition</a>, ... ]</i>,
    "<a href="#eastwestplacementsubnet" title="EastWestPlacementSubnet">EastWestPlacementSubnet</a>" : <i>[ <a href="eastwestplacementsubnetdefinition.md">EastWestPlacementSubnetDefinition</a>, ... ]</i>,
    "<a href="#seexcludeattributes" title="SeExcludeAttributes">SeExcludeAttributes</a>" : <i>[ <a href="seexcludeattributesdefinition.md">SeExcludeAttributesDefinition</a>, ... ]</i>,
    "<a href="#seincludeattributes" title="SeIncludeAttributes">SeIncludeAttributes</a>" : <i>[ <a href="seincludeattributesdefinition.md">SeIncludeAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#appsyncfrequency" title="AppSyncFrequency">AppSyncFrequency</a>: <i>Double</i>
<a href="#catlskeyandcertificateref" title="CaTlsKeyAndCertificateRef">CaTlsKeyAndCertificateRef</a>: <i>String</i>
<a href="#clienttlskeyandcertificateref" title="ClientTlsKeyAndCertificateRef">ClientTlsKeyAndCertificateRef</a>: <i>String</i>
<a href="#containerportmatchhttpservice" title="ContainerPortMatchHttpService">ContainerPortMatchHttpService</a>: <i>Boolean</i>
<a href="#coredumpdirectory" title="CoredumpDirectory">CoredumpDirectory</a>: <i>String</i>
<a href="#disableautobackendservicesync" title="DisableAutoBackendServiceSync">DisableAutoBackendServiceSync</a>: <i>Boolean</i>
<a href="#disableautofrontendservicesync" title="DisableAutoFrontendServiceSync">DisableAutoFrontendServiceSync</a>: <i>Boolean</i>
<a href="#disableautosecreation" title="DisableAutoSeCreation">DisableAutoSeCreation</a>: <i>Boolean</i>
<a href="#enableeventsubscription" title="EnableEventSubscription">EnableEventSubscription</a>: <i>Boolean</i>
<a href="#feproxycontainerportasservice" title="FeproxyContainerPortAsService">FeproxyContainerPortAsService</a>: <i>Boolean</i>
<a href="#feproxyvipsenableproxyarp" title="FeproxyVipsEnableProxyArp">FeproxyVipsEnableProxyArp</a>: <i>Boolean</i>
<a href="#fleetendpoint" title="FleetEndpoint">FleetEndpoint</a>: <i>String</i>
<a href="#httpcontainerports" title="HttpContainerPorts">HttpContainerPorts</a>: <i>
      - Double</i>
<a href="#sedeploymentmethod" title="SeDeploymentMethod">SeDeploymentMethod</a>: <i>String</i>
<a href="#sespawnrate" title="SeSpawnRate">SeSpawnRate</a>: <i>Double</i>
<a href="#sevolume" title="SeVolume">SeVolume</a>: <i>String</i>
<a href="#servicesaccessibleallinterfaces" title="ServicesAccessibleAllInterfaces">ServicesAccessibleAllInterfaces</a>: <i>Boolean</i>
<a href="#sshuserref" title="SshUserRef">SshUserRef</a>: <i>String</i>
<a href="#ucpnodes" title="UcpNodes">UcpNodes</a>: <i>
      - String</i>
<a href="#usecontaineripport" title="UseContainerIpPort">UseContainerIpPort</a>: <i>Boolean</i>
<a href="#usecontrollerimage" title="UseControllerImage">UseControllerImage</a>: <i>Boolean</i>
<a href="#dockerregistryse" title="DockerRegistrySe">DockerRegistrySe</a>: <i>
      - <a href="dockerregistrysedefinition.md">DockerRegistrySeDefinition</a></i>
<a href="#eastwestplacementsubnet" title="EastWestPlacementSubnet">EastWestPlacementSubnet</a>: <i>
      - <a href="eastwestplacementsubnetdefinition.md">EastWestPlacementSubnetDefinition</a></i>
<a href="#seexcludeattributes" title="SeExcludeAttributes">SeExcludeAttributes</a>: <i>
      - <a href="seexcludeattributesdefinition.md">SeExcludeAttributesDefinition</a></i>
<a href="#seincludeattributes" title="SeIncludeAttributes">SeIncludeAttributes</a>: <i>
      - <a href="seincludeattributesdefinition.md">SeIncludeAttributesDefinition</a></i>
</pre>

## Properties

#### AppSyncFrequency

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaTlsKeyAndCertificateRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientTlsKeyAndCertificateRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerPortMatchHttpService

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoredumpDirectory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAutoBackendServiceSync

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAutoFrontendServiceSync

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAutoSeCreation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEventSubscription

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeproxyContainerPortAsService

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeproxyVipsEnableProxyArp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpContainerPorts

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDeploymentMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeSpawnRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeVolume

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesAccessibleAllInterfaces

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUserRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcpNodes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseContainerIpPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseControllerImage

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerRegistrySe

_Required_: No

_Type_: List of <a href="dockerregistrysedefinition.md">DockerRegistrySeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EastWestPlacementSubnet

_Required_: No

_Type_: List of <a href="eastwestplacementsubnetdefinition.md">EastWestPlacementSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeExcludeAttributes

_Required_: No

_Type_: List of <a href="seexcludeattributesdefinition.md">SeExcludeAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeIncludeAttributes

_Required_: No

_Type_: List of <a href="seincludeattributesdefinition.md">SeIncludeAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

