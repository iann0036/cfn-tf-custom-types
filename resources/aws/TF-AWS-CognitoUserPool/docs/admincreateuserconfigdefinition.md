# TF::AWS::CognitoUserPool AdminCreateUserConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowadmincreateuseronly" title="AllowAdminCreateUserOnly">AllowAdminCreateUserOnly</a>" : <i>Boolean</i>,
    "<a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>" : <i>[ <a href="invitemessagetemplatedefinition.md">InviteMessageTemplateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowadmincreateuseronly" title="AllowAdminCreateUserOnly">AllowAdminCreateUserOnly</a>: <i>Boolean</i>
<a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>: <i>
      - <a href="invitemessagetemplatedefinition.md">InviteMessageTemplateDefinition</a></i>
</pre>

## Properties

#### AllowAdminCreateUserOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InviteMessageTemplate

_Required_: No

_Type_: List of <a href="invitemessagetemplatedefinition.md">InviteMessageTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

