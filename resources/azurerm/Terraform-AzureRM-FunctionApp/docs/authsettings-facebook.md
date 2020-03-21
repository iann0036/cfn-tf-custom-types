# Terraform::AzureRM::FunctionApp AuthSettings Facebook

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
    "<a href="#appsecret" title="AppSecret">AppSecret</a>" : <i>String</i>,
    "<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#appid" title="AppId">AppId</a>: <i>String</i>
<a href="#appsecret" title="AppSecret">AppSecret</a>: <i>String</i>
<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>: <i>
      - String</i>
</pre>

## Properties

#### AppId

The App ID of the Facebook app used for login.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSecret

The App Secret of the Facebook app used for Facebook Login.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthScopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

