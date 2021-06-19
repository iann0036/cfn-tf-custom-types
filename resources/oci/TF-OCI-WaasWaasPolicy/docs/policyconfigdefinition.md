# TF::OCI::WaasWaasPolicy PolicyConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
    "<a href="#ciphergroup" title="CipherGroup">CipherGroup</a>" : <i>String</i>,
    "<a href="#clientaddressheader" title="ClientAddressHeader">ClientAddressHeader</a>" : <i>String</i>,
    "<a href="#isbehindcdn" title="IsBehindCdn">IsBehindCdn</a>" : <i>Boolean</i>,
    "<a href="#iscachecontrolrespected" title="IsCacheControlRespected">IsCacheControlRespected</a>" : <i>Boolean</i>,
    "<a href="#ishttpsenabled" title="IsHttpsEnabled">IsHttpsEnabled</a>" : <i>Boolean</i>,
    "<a href="#ishttpsforced" title="IsHttpsForced">IsHttpsForced</a>" : <i>Boolean</i>,
    "<a href="#isorigincompressionenabled" title="IsOriginCompressionEnabled">IsOriginCompressionEnabled</a>" : <i>Boolean</i>,
    "<a href="#isresponsebufferingenabled" title="IsResponseBufferingEnabled">IsResponseBufferingEnabled</a>" : <i>Boolean</i>,
    "<a href="#issnienabled" title="IsSniEnabled">IsSniEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsprotocols" title="TlsProtocols">TlsProtocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#websocketpathprefixes" title="WebsocketPathPrefixes">WebsocketPathPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#healthchecks" title="HealthChecks">HealthChecks</a>" : <i>[ <a href="healthchecksdefinition.md">HealthChecksDefinition</a>, ... ]</i>,
    "<a href="#loadbalancingmethod" title="LoadBalancingMethod">LoadBalancingMethod</a>" : <i>[ <a href="loadbalancingmethoddefinition.md">LoadBalancingMethodDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
<a href="#ciphergroup" title="CipherGroup">CipherGroup</a>: <i>String</i>
<a href="#clientaddressheader" title="ClientAddressHeader">ClientAddressHeader</a>: <i>String</i>
<a href="#isbehindcdn" title="IsBehindCdn">IsBehindCdn</a>: <i>Boolean</i>
<a href="#iscachecontrolrespected" title="IsCacheControlRespected">IsCacheControlRespected</a>: <i>Boolean</i>
<a href="#ishttpsenabled" title="IsHttpsEnabled">IsHttpsEnabled</a>: <i>Boolean</i>
<a href="#ishttpsforced" title="IsHttpsForced">IsHttpsForced</a>: <i>Boolean</i>
<a href="#isorigincompressionenabled" title="IsOriginCompressionEnabled">IsOriginCompressionEnabled</a>: <i>Boolean</i>
<a href="#isresponsebufferingenabled" title="IsResponseBufferingEnabled">IsResponseBufferingEnabled</a>: <i>Boolean</i>
<a href="#issnienabled" title="IsSniEnabled">IsSniEnabled</a>: <i>Boolean</i>
<a href="#tlsprotocols" title="TlsProtocols">TlsProtocols</a>: <i>
      - String</i>
<a href="#websocketpathprefixes" title="WebsocketPathPrefixes">WebsocketPathPrefixes</a>: <i>
      - String</i>
<a href="#healthchecks" title="HealthChecks">HealthChecks</a>: <i>
      - <a href="healthchecksdefinition.md">HealthChecksDefinition</a></i>
<a href="#loadbalancingmethod" title="LoadBalancingMethod">LoadBalancingMethod</a>: <i>
      - <a href="loadbalancingmethoddefinition.md">LoadBalancingMethodDefinition</a></i>
</pre>

## Properties

#### CertificateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAddressHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsBehindCdn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCacheControlRespected

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHttpsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHttpsForced

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOriginCompressionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsResponseBufferingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSniEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsProtocols

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsocketPathPrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthChecks

_Required_: No

_Type_: List of <a href="healthchecksdefinition.md">HealthChecksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingMethod

_Required_: No

_Type_: List of <a href="loadbalancingmethoddefinition.md">LoadBalancingMethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

