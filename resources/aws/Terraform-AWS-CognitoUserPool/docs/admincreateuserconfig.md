# Terraform::AWS::CognitoUserPool AdminCreateUserConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowadmincreateuseronly" title="AllowAdminCreateUserOnly">AllowAdminCreateUserOnly</a>" : <i>Boolean</i>,
    "<a href="#unusedaccountvaliditydays" title="UnusedAccountValidityDays">UnusedAccountValidityDays</a>" : <i>Double</i>,
    "<a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>" : <i>[ <a href="admincreateuserconfig-invitemessagetemplate.md">InviteMessageTemplate</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowadmincreateuseronly" title="AllowAdminCreateUserOnly">AllowAdminCreateUserOnly</a>: <i>Boolean</i>
<a href="#unusedaccountvaliditydays" title="UnusedAccountValidityDays">UnusedAccountValidityDays</a>: <i>Double</i>
<a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>: <i>
      - <a href="admincreateuserconfig-invitemessagetemplate.md">InviteMessageTemplate</a></i>
</pre>

## Properties

#### AllowAdminCreateUserOnly

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnusedAccountValidityDays

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InviteMessageTemplate

_Required_: No
_Type_: List of <a href="admincreateuserconfig-invitemessagetemplate.md">InviteMessageTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

