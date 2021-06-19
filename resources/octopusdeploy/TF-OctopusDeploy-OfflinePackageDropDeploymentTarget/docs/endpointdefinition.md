# TF::OctopusDeploy::OfflinePackageDropDeploymentTarget EndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aadclientcredentialsecret" title="AadClientCredentialSecret">AadClientCredentialSecret</a>" : <i>String</i>,
    "<a href="#aadcredentialtype" title="AadCredentialType">AadCredentialType</a>" : <i>String</i>,
    "<a href="#aadusercredentialusername" title="AadUserCredentialUsername">AadUserCredentialUsername</a>" : <i>String</i>,
    "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
    "<a href="#applicationsdirectory" title="ApplicationsDirectory">ApplicationsDirectory</a>" : <i>String</i>,
    "<a href="#certificatesignaturealgorithm" title="CertificateSignatureAlgorithm">CertificateSignatureAlgorithm</a>" : <i>String</i>,
    "<a href="#certificatestorelocation" title="CertificateStoreLocation">CertificateStoreLocation</a>" : <i>String</i>,
    "<a href="#certificatestorename" title="CertificateStoreName">CertificateStoreName</a>" : <i>String</i>,
    "<a href="#clientcertificatevariable" title="ClientCertificateVariable">ClientCertificateVariable</a>" : <i>String</i>,
    "<a href="#cloudservicename" title="CloudServiceName">CloudServiceName</a>" : <i>String</i>,
    "<a href="#clustercertificate" title="ClusterCertificate">ClusterCertificate</a>" : <i>String</i>,
    "<a href="#clusterurl" title="ClusterUrl">ClusterUrl</a>" : <i>String</i>,
    "<a href="#communicationstyle" title="CommunicationStyle">CommunicationStyle</a>" : <i>String</i>,
    "<a href="#connectionendpoint" title="ConnectionEndpoint">ConnectionEndpoint</a>" : <i>String</i>,
    "<a href="#defaultworkerpoolid" title="DefaultWorkerPoolId">DefaultWorkerPoolId</a>" : <i>String</i>,
    "<a href="#dotnetcoreplatform" title="DotNetCorePlatform">DotNetCorePlatform</a>" : <i>String</i>,
    "<a href="#fingerprint" title="Fingerprint">Fingerprint</a>" : <i>String</i>,
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#proxyid" title="ProxyId">ProxyId</a>" : <i>String</i>,
    "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
    "<a href="#runningincontainer" title="RunningInContainer">RunningInContainer</a>" : <i>Boolean</i>,
    "<a href="#securitymode" title="SecurityMode">SecurityMode</a>" : <i>String</i>,
    "<a href="#servercertificatethumbprint" title="ServerCertificateThumbprint">ServerCertificateThumbprint</a>" : <i>String</i>,
    "<a href="#skiptlsverification" title="SkipTlsVerification">SkipTlsVerification</a>" : <i>Boolean</i>,
    "<a href="#slot" title="Slot">Slot</a>" : <i>String</i>,
    "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
    "<a href="#swapifpossible" title="SwapIfPossible">SwapIfPossible</a>" : <i>Boolean</i>,
    "<a href="#thumbprint" title="Thumbprint">Thumbprint</a>" : <i>String</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
    "<a href="#usecurrentinstancecount" title="UseCurrentInstanceCount">UseCurrentInstanceCount</a>" : <i>Boolean</i>,
    "<a href="#webappname" title="WebAppName">WebAppName</a>" : <i>String</i>,
    "<a href="#webappslotname" title="WebAppSlotName">WebAppSlotName</a>" : <i>String</i>,
    "<a href="#workingdirectory" title="WorkingDirectory">WorkingDirectory</a>" : <i>String</i>,
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authenticationdefinition.md">AuthenticationDefinition</a>, ... ]</i>,
    "<a href="#container" title="Container">Container</a>" : <i>[ <a href="containerdefinition.md">ContainerDefinition</a>, ... ]</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destinationdefinition.md">DestinationDefinition</a>, ... ]</i>,
    "<a href="#tentacleversiondetails" title="TentacleVersionDetails">TentacleVersionDetails</a>" : <i>[ <a href="tentacleversiondetailsdefinition.md">TentacleVersionDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aadclientcredentialsecret" title="AadClientCredentialSecret">AadClientCredentialSecret</a>: <i>String</i>
<a href="#aadcredentialtype" title="AadCredentialType">AadCredentialType</a>: <i>String</i>
<a href="#aadusercredentialusername" title="AadUserCredentialUsername">AadUserCredentialUsername</a>: <i>String</i>
<a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
<a href="#applicationsdirectory" title="ApplicationsDirectory">ApplicationsDirectory</a>: <i>String</i>
<a href="#certificatesignaturealgorithm" title="CertificateSignatureAlgorithm">CertificateSignatureAlgorithm</a>: <i>String</i>
<a href="#certificatestorelocation" title="CertificateStoreLocation">CertificateStoreLocation</a>: <i>String</i>
<a href="#certificatestorename" title="CertificateStoreName">CertificateStoreName</a>: <i>String</i>
<a href="#clientcertificatevariable" title="ClientCertificateVariable">ClientCertificateVariable</a>: <i>String</i>
<a href="#cloudservicename" title="CloudServiceName">CloudServiceName</a>: <i>String</i>
<a href="#clustercertificate" title="ClusterCertificate">ClusterCertificate</a>: <i>String</i>
<a href="#clusterurl" title="ClusterUrl">ClusterUrl</a>: <i>String</i>
<a href="#communicationstyle" title="CommunicationStyle">CommunicationStyle</a>: <i>String</i>
<a href="#connectionendpoint" title="ConnectionEndpoint">ConnectionEndpoint</a>: <i>String</i>
<a href="#defaultworkerpoolid" title="DefaultWorkerPoolId">DefaultWorkerPoolId</a>: <i>String</i>
<a href="#dotnetcoreplatform" title="DotNetCorePlatform">DotNetCorePlatform</a>: <i>String</i>
<a href="#fingerprint" title="Fingerprint">Fingerprint</a>: <i>String</i>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#proxyid" title="ProxyId">ProxyId</a>: <i>String</i>
<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
<a href="#runningincontainer" title="RunningInContainer">RunningInContainer</a>: <i>Boolean</i>
<a href="#securitymode" title="SecurityMode">SecurityMode</a>: <i>String</i>
<a href="#servercertificatethumbprint" title="ServerCertificateThumbprint">ServerCertificateThumbprint</a>: <i>String</i>
<a href="#skiptlsverification" title="SkipTlsVerification">SkipTlsVerification</a>: <i>Boolean</i>
<a href="#slot" title="Slot">Slot</a>: <i>String</i>
<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
<a href="#swapifpossible" title="SwapIfPossible">SwapIfPossible</a>: <i>Boolean</i>
<a href="#thumbprint" title="Thumbprint">Thumbprint</a>: <i>String</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
<a href="#usecurrentinstancecount" title="UseCurrentInstanceCount">UseCurrentInstanceCount</a>: <i>Boolean</i>
<a href="#webappname" title="WebAppName">WebAppName</a>: <i>String</i>
<a href="#webappslotname" title="WebAppSlotName">WebAppSlotName</a>: <i>String</i>
<a href="#workingdirectory" title="WorkingDirectory">WorkingDirectory</a>: <i>String</i>
<a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authenticationdefinition.md">AuthenticationDefinition</a></i>
<a href="#container" title="Container">Container</a>: <i>
      - <a href="containerdefinition.md">ContainerDefinition</a></i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destinationdefinition.md">DestinationDefinition</a></i>
<a href="#tentacleversiondetails" title="TentacleVersionDetails">TentacleVersionDetails</a>: <i>
      - <a href="tentacleversiondetailsdefinition.md">TentacleVersionDetailsDefinition</a></i>
</pre>

## Properties

#### AadClientCredentialSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadCredentialType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadUserCredentialUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationsDirectory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSignatureAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateStoreLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateStoreName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateVariable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudServiceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunicationStyle

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultWorkerPoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DotNetCorePlatform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fingerprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunningInContainer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateThumbprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipTlsVerification

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwapIfPossible

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCurrentInstanceCount

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAppName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAppSlotName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDirectory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authenticationdefinition.md">AuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="containerdefinition.md">ContainerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destinationdefinition.md">DestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TentacleVersionDetails

_Required_: No

_Type_: List of <a href="tentacleversiondetailsdefinition.md">TentacleVersionDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

