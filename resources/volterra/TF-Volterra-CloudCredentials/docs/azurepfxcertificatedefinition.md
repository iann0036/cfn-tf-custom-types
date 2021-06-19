# TF::Volterra::CloudCredentials AzurePfxCertificateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>" : <i>String</i>,
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>[ <a href="passworddefinition.md">PasswordDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>: <i>String</i>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>
      - <a href="passworddefinition.md">PasswordDefinition</a></i>
</pre>

## Properties

#### CertificateUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: List of <a href="passworddefinition.md">PasswordDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

