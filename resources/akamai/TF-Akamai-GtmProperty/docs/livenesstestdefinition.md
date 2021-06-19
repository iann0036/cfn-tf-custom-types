# TF::Akamai::GtmProperty LivenessTestDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#answersrequired" title="AnswersRequired">AnswersRequired</a>" : <i>Boolean</i>,
    "<a href="#disablenonstandardportwarning" title="DisableNonstandardPortWarning">DisableNonstandardPortWarning</a>" : <i>Boolean</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#errorpenalty" title="ErrorPenalty">ErrorPenalty</a>" : <i>Double</i>,
    "<a href="#httperror3xx" title="HttpError3xx">HttpError3xx</a>" : <i>Boolean</i>,
    "<a href="#httperror4xx" title="HttpError4xx">HttpError4xx</a>" : <i>Boolean</i>,
    "<a href="#httperror5xx" title="HttpError5xx">HttpError5xx</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#peercertificateverification" title="PeerCertificateVerification">PeerCertificateVerification</a>" : <i>Boolean</i>,
    "<a href="#recursionrequested" title="RecursionRequested">RecursionRequested</a>" : <i>Boolean</i>,
    "<a href="#requeststring" title="RequestString">RequestString</a>" : <i>String</i>,
    "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
    "<a href="#responsestring" title="ResponseString">ResponseString</a>" : <i>String</i>,
    "<a href="#sslclientcertificate" title="SslClientCertificate">SslClientCertificate</a>" : <i>String</i>,
    "<a href="#sslclientprivatekey" title="SslClientPrivateKey">SslClientPrivateKey</a>" : <i>String</i>,
    "<a href="#testinterval" title="TestInterval">TestInterval</a>" : <i>Double</i>,
    "<a href="#testobject" title="TestObject">TestObject</a>" : <i>String</i>,
    "<a href="#testobjectpassword" title="TestObjectPassword">TestObjectPassword</a>" : <i>String</i>,
    "<a href="#testobjectport" title="TestObjectPort">TestObjectPort</a>" : <i>Double</i>,
    "<a href="#testobjectprotocol" title="TestObjectProtocol">TestObjectProtocol</a>" : <i>String</i>,
    "<a href="#testobjectusername" title="TestObjectUsername">TestObjectUsername</a>" : <i>String</i>,
    "<a href="#testtimeout" title="TestTimeout">TestTimeout</a>" : <i>Double</i>,
    "<a href="#timeoutpenalty" title="TimeoutPenalty">TimeoutPenalty</a>" : <i>Double</i>,
    "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ <a href="httpheaderdefinition.md">HttpHeaderDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#answersrequired" title="AnswersRequired">AnswersRequired</a>: <i>Boolean</i>
<a href="#disablenonstandardportwarning" title="DisableNonstandardPortWarning">DisableNonstandardPortWarning</a>: <i>Boolean</i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#errorpenalty" title="ErrorPenalty">ErrorPenalty</a>: <i>Double</i>
<a href="#httperror3xx" title="HttpError3xx">HttpError3xx</a>: <i>Boolean</i>
<a href="#httperror4xx" title="HttpError4xx">HttpError4xx</a>: <i>Boolean</i>
<a href="#httperror5xx" title="HttpError5xx">HttpError5xx</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#peercertificateverification" title="PeerCertificateVerification">PeerCertificateVerification</a>: <i>Boolean</i>
<a href="#recursionrequested" title="RecursionRequested">RecursionRequested</a>: <i>Boolean</i>
<a href="#requeststring" title="RequestString">RequestString</a>: <i>String</i>
<a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
<a href="#responsestring" title="ResponseString">ResponseString</a>: <i>String</i>
<a href="#sslclientcertificate" title="SslClientCertificate">SslClientCertificate</a>: <i>String</i>
<a href="#sslclientprivatekey" title="SslClientPrivateKey">SslClientPrivateKey</a>: <i>String</i>
<a href="#testinterval" title="TestInterval">TestInterval</a>: <i>Double</i>
<a href="#testobject" title="TestObject">TestObject</a>: <i>String</i>
<a href="#testobjectpassword" title="TestObjectPassword">TestObjectPassword</a>: <i>String</i>
<a href="#testobjectport" title="TestObjectPort">TestObjectPort</a>: <i>Double</i>
<a href="#testobjectprotocol" title="TestObjectProtocol">TestObjectProtocol</a>: <i>String</i>
<a href="#testobjectusername" title="TestObjectUsername">TestObjectUsername</a>: <i>String</i>
<a href="#testtimeout" title="TestTimeout">TestTimeout</a>: <i>Double</i>
<a href="#timeoutpenalty" title="TimeoutPenalty">TimeoutPenalty</a>: <i>Double</i>
<a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - <a href="httpheaderdefinition.md">HttpHeaderDefinition</a></i>
</pre>

## Properties

#### AnswersRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableNonstandardPortWarning

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorPenalty

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpError3xx

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpError4xx

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpError5xx

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerCertificateVerification

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecursionRequested

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientPrivateKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestInterval

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestObject

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestObjectPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestObjectPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestObjectProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestObjectUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTimeout

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutPenalty

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of <a href="httpheaderdefinition.md">HttpHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

