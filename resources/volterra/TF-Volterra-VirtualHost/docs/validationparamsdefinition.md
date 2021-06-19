# TF::Volterra::VirtualHost ValidationParamsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#skiphostnameverification" title="SkipHostnameVerification">SkipHostnameVerification</a>" : <i>Boolean</i>,
    "<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>" : <i>String</i>,
    "<a href="#usevolterratrustedcaurl" title="UseVolterraTrustedCaUrl">UseVolterraTrustedCaUrl</a>" : <i>Boolean</i>,
    "<a href="#verifysubjectaltnames" title="VerifySubjectAltNames">VerifySubjectAltNames</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#skiphostnameverification" title="SkipHostnameVerification">SkipHostnameVerification</a>: <i>Boolean</i>
<a href="#trustedcaurl" title="TrustedCaUrl">TrustedCaUrl</a>: <i>String</i>
<a href="#usevolterratrustedcaurl" title="UseVolterraTrustedCaUrl">UseVolterraTrustedCaUrl</a>: <i>Boolean</i>
<a href="#verifysubjectaltnames" title="VerifySubjectAltNames">VerifySubjectAltNames</a>: <i>
      - String</i>
</pre>

## Properties

#### SkipHostnameVerification

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedCaUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseVolterraTrustedCaUrl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifySubjectAltNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

