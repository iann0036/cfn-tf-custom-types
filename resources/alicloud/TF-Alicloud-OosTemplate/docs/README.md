# TF::Alicloud::OosTemplate

Provides a OOS Template resource. For information about Alicloud OOS Template and how to use it, see [What is Resource Alicloud OOS Template](https://www.alibabacloud.com/help/doc-detail/120761.htm).

-> **NOTE:** Available in 1.92.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::OosTemplate",
    "Properties" : {
        "<a href="#autodeleteexecutions" title="AutoDeleteExecutions">AutoDeleteExecutions</a>" : <i>Boolean</i>,
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#versionname" title="VersionName">VersionName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::OosTemplate
Properties:
    <a href="#autodeleteexecutions" title="AutoDeleteExecutions">AutoDeleteExecutions</a>: <i>Boolean</i>
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#versionname" title="VersionName">VersionName</a>: <i>String</i>
</pre>

## Properties

#### AutoDeleteExecutions

When deleting a template, whether to delete its related executions. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

The content of the template. The template must be in the JSON or YAML format. Maximum size: 64 KB.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

The name of the template. The template name can be up to 200 characters in length. The name can contain letters, digits, hyphens (-), and underscores (_). It cannot start with `ALIYUN`, `ACS`, `ALIBABA`, or `ALICLOUD`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionName

The name of template version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### Description

Returns the <code>Description</code> value.

#### HasTrigger

Returns the <code>HasTrigger</code> value.

#### Id

Returns the <code>Id</code> value.

#### ShareType

Returns the <code>ShareType</code> value.

#### TemplateFormat

Returns the <code>TemplateFormat</code> value.

#### TemplateId

Returns the <code>TemplateId</code> value.

#### TemplateType

Returns the <code>TemplateType</code> value.

#### TemplateVersion

Returns the <code>TemplateVersion</code> value.

#### UpdatedBy

Returns the <code>UpdatedBy</code> value.

#### UpdatedDate

Returns the <code>UpdatedDate</code> value.

