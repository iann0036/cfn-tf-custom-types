# TF::NSXT::LbHttpVirtualServer ServerSslDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caids" title="CaIds">CaIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>" : <i>Double</i>,
    "<a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>" : <i>String</i>,
    "<a href="#crlids" title="CrlIds">CrlIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#serverauth" title="ServerAuth">ServerAuth</a>" : <i>Boolean</i>,
    "<a href="#serversslprofileid" title="ServerSslProfileId">ServerSslProfileId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#caids" title="CaIds">CaIds</a>: <i>
      - String</i>
<a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>: <i>Double</i>
<a href="#clientcertificateid" title="ClientCertificateId">ClientCertificateId</a>: <i>String</i>
<a href="#crlids" title="CrlIds">CrlIds</a>: <i>
      - String</i>
<a href="#serverauth" title="ServerAuth">ServerAuth</a>: <i>Boolean</i>
<a href="#serversslprofileid" title="ServerSslProfileId">ServerSslProfileId</a>: <i>String</i>
</pre>

## Properties

#### CaIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateChainDepth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSslProfileId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

