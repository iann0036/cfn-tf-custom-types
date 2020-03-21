# Terraform::NSXT::LbHttpVirtualServer ClientSsl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caids" title="CaIds">CaIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>" : <i>Double</i>,
    "<a href="#clientauth" title="ClientAuth">ClientAuth</a>" : <i>Boolean</i>,
    "<a href="#clientsslprofileid" title="ClientSslProfileId">ClientSslProfileId</a>" : <i>String</i>,
    "<a href="#crlids" title="CrlIds">CrlIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#defaultcertificateid" title="DefaultCertificateId">DefaultCertificateId</a>" : <i>String</i>,
    "<a href="#snicertificateids" title="SniCertificateIds">SniCertificateIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#caids" title="CaIds">CaIds</a>: <i>
      - String</i>
<a href="#certificatechaindepth" title="CertificateChainDepth">CertificateChainDepth</a>: <i>Double</i>
<a href="#clientauth" title="ClientAuth">ClientAuth</a>: <i>Boolean</i>
<a href="#clientsslprofileid" title="ClientSslProfileId">ClientSslProfileId</a>: <i>String</i>
<a href="#crlids" title="CrlIds">CrlIds</a>: <i>
      - String</i>
<a href="#defaultcertificateid" title="DefaultCertificateId">DefaultCertificateId</a>: <i>String</i>
<a href="#snicertificateids" title="SniCertificateIds">SniCertificateIds</a>: <i>
      - String</i>
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

#### ClientAuth

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSslProfileId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCertificateId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniCertificateIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

