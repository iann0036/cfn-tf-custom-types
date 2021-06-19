# TF::AzureDevOps::ServiceendpointGithub AuthOauthDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#oauthconfigurationid" title="OauthConfigurationId">OauthConfigurationId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#oauthconfigurationid" title="OauthConfigurationId">OauthConfigurationId</a>: <i>String</i>
</pre>

## Properties

#### OauthConfigurationId

**NOTE: Github OAuth flow can not be performed via terraform. You must create this on Azure DevOps and then import it.** The OAuth Configuration ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

