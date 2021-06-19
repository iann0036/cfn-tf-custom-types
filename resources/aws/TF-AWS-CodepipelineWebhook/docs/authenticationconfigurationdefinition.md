# TF::AWS::CodepipelineWebhook AuthenticationConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowediprange" title="AllowedIpRange">AllowedIpRange</a>" : <i>String</i>,
    "<a href="#secrettoken" title="SecretToken">SecretToken</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowediprange" title="AllowedIpRange">AllowedIpRange</a>: <i>String</i>
<a href="#secrettoken" title="SecretToken">SecretToken</a>: <i>String</i>
</pre>

## Properties

#### AllowedIpRange

A valid CIDR block for `IP` filtering. Required for `IP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretToken

The shared secret for the GitHub repository webhook. Set this as `secret` in your `github_repository_webhook`'s `configuration` block. Required for `GITHUB_HMAC`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

