# Terraform::Google::IdentityPlatformInboundSamlConfig IdpConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>" : <i>String</i>,
    "<a href="#signrequest" title="SignRequest">SignRequest</a>" : <i>Boolean</i>,
    "<a href="#ssourl" title="SsoUrl">SsoUrl</a>" : <i>String</i>,
    "<a href="#idpcertificates" title="IdpCertificates">IdpCertificates</a>" : <i>[ <a href="idpconfig-idpcertificates.md">IdpCertificates</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>: <i>String</i>
<a href="#signrequest" title="SignRequest">SignRequest</a>: <i>Boolean</i>
<a href="#ssourl" title="SsoUrl">SsoUrl</a>: <i>String</i>
<a href="#idpcertificates" title="IdpCertificates">IdpCertificates</a>: <i>
      - <a href="idpconfig-idpcertificates.md">IdpCertificates</a></i>
</pre>

## Properties

#### IdpEntityId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignRequest

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoUrl

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpCertificates

_Required_: No
_Type_: List of <a href="idpconfig-idpcertificates.md">IdpCertificates</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

