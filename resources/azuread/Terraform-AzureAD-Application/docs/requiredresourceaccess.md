# Terraform::AzureAD::Application RequiredResourceAccess

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resourceappid" title="ResourceAppId">ResourceAppId</a>" : <i>String</i>,
    "<a href="#resourceaccess" title="ResourceAccess">ResourceAccess</a>" : <i>[ <a href="requiredresourceaccess-resourceaccess.md">ResourceAccess</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#resourceappid" title="ResourceAppId">ResourceAppId</a>: <i>String</i>
<a href="#resourceaccess" title="ResourceAccess">ResourceAccess</a>: <i>
      - <a href="requiredresourceaccess-resourceaccess.md">ResourceAccess</a></i>
</pre>

## Properties

#### ResourceAppId

The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceAccess

_Required_: No

_Type_: List of <a href="requiredresourceaccess-resourceaccess.md">ResourceAccess</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

