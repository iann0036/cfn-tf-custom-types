# TF::VSphere::VirtualMachine OvfDeployDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowunverifiedsslcert" title="AllowUnverifiedSslCert">AllowUnverifiedSslCert</a>" : <i>Boolean</i>,
    "<a href="#deploymentoption" title="DeploymentOption">DeploymentOption</a>" : <i>String</i>,
    "<a href="#diskprovisioning" title="DiskProvisioning">DiskProvisioning</a>" : <i>String</i>,
    "<a href="#enablehiddenproperties" title="EnableHiddenProperties">EnableHiddenProperties</a>" : <i>Boolean</i>,
    "<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>" : <i>String</i>,
    "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
    "<a href="#localovfpath" title="LocalOvfPath">LocalOvfPath</a>" : <i>String</i>,
    "<a href="#ovfnetworkmap" title="OvfNetworkMap">OvfNetworkMap</a>" : <i>[ <a href="ovfnetworkmapdefinition.md">OvfNetworkMapDefinition</a>, ... ]</i>,
    "<a href="#remoteovfurl" title="RemoteOvfUrl">RemoteOvfUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowunverifiedsslcert" title="AllowUnverifiedSslCert">AllowUnverifiedSslCert</a>: <i>Boolean</i>
<a href="#deploymentoption" title="DeploymentOption">DeploymentOption</a>: <i>String</i>
<a href="#diskprovisioning" title="DiskProvisioning">DiskProvisioning</a>: <i>String</i>
<a href="#enablehiddenproperties" title="EnableHiddenProperties">EnableHiddenProperties</a>: <i>Boolean</i>
<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>: <i>String</i>
<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
<a href="#localovfpath" title="LocalOvfPath">LocalOvfPath</a>: <i>String</i>
<a href="#ovfnetworkmap" title="OvfNetworkMap">OvfNetworkMap</a>: <i>
      - <a href="ovfnetworkmapdefinition.md">OvfNetworkMapDefinition</a></i>
<a href="#remoteovfurl" title="RemoteOvfUrl">RemoteOvfUrl</a>: <i>String</i>
</pre>

## Properties

#### AllowUnverifiedSslCert

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentOption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskProvisioning

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHiddenProperties

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllocationPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalOvfPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvfNetworkMap

_Required_: No

_Type_: List of <a href="ovfnetworkmapdefinition.md">OvfNetworkMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteOvfUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

