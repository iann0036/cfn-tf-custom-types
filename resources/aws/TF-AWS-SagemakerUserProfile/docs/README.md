# TF::AWS::SagemakerUserProfile

Provides a Sagemaker User Profile resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SagemakerUserProfile",
    "Properties" : {
        "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
        "<a href="#singlesignonuseridentifier" title="SingleSignOnUserIdentifier">SingleSignOnUserIdentifier</a>" : <i>String</i>,
        "<a href="#singlesignonuservalue" title="SingleSignOnUserValue">SingleSignOnUserValue</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#userprofilename" title="UserProfileName">UserProfileName</a>" : <i>String</i>,
        "<a href="#usersettings" title="UserSettings">UserSettings</a>" : <i>[ <a href="usersettingsdefinition.md">UserSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SagemakerUserProfile
Properties:
    <a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
    <a href="#singlesignonuseridentifier" title="SingleSignOnUserIdentifier">SingleSignOnUserIdentifier</a>: <i>String</i>
    <a href="#singlesignonuservalue" title="SingleSignOnUserValue">SingleSignOnUserValue</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#userprofilename" title="UserProfileName">UserProfileName</a>: <i>String</i>
    <a href="#usersettings" title="UserSettings">UserSettings</a>: <i>
      - <a href="usersettingsdefinition.md">UserSettingsDefinition</a></i>
</pre>

## Properties

#### DomainId

The ID of the associated Domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleSignOnUserIdentifier

A specifier for the type of value specified in `single_sign_on_user_value`. Currently, the only supported value is `UserName`. If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleSignOnUserValue

The username of the associated AWS Single Sign-On User for this User Profile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserProfileName

The name for the User Profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSettings

_Required_: No

_Type_: List of <a href="usersettingsdefinition.md">UserSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### HomeEfsFileSystemUid

Returns the <code>HomeEfsFileSystemUid</code> value.

#### Id

Returns the <code>Id</code> value.

