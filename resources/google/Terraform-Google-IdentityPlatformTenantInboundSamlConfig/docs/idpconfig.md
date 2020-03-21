# Terraform::Google::IdentityPlatformTenantInboundSamlConfig IdpConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>" : <i>String</i>,
    "<a href="#signrequest" title="SignRequest">SignRequest</a>" : <i>Boolean</i>,
    "<a href="#ssourl" title="SsoUrl">SsoUrl</a>" : <i>String</i>,
    "<a href="#idpcertificates" title="IdpCertificates">IdpCertificates</a>" : <i>[ &lt;a href=&#34;idpconfig-idpcertificates.md&#34;&gt;IdpCertificates&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>: <i>String</i>
<a href="#signrequest" title="SignRequest">SignRequest</a>: <i>Boolean</i>
<a href="#ssourl" title="SsoUrl">SsoUrl</a>: <i>String</i>
<a href="#idpcertificates" title="IdpCertificates">IdpCertificates</a>: <i>
      - &lt;a href=&#34;idpconfig-idpcertificates.md&#34;&gt;IdpCertificates&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;idpconfig-idpcertificates.md&#34;&gt;IdpCertificates&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

