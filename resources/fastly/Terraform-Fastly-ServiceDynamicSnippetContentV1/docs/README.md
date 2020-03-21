# Terraform::Fastly::ServiceDynamicSnippetContentV1

Defines content that represents blocks of VCL logic that is inserted into your service.  This resource will populate the content of a dynamic snippet and allow it to be manged without the creation of a new service verison. 
 
~> **Warning:** Terraform will take precedence over any changes you make through the API. Such changes are likely to be reversed if you run Terraform again.  

If Terraform is being used to populate the initial content of a dynamic snippet which you intend to manage via the API, then the lifecycle `ignore_changes` field can be used with the resource.  An example of this configuration is provided below.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Fastly::ServiceDynamicSnippetContentV1",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#snippetid" title="SnippetId">SnippetId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Fastly::ServiceDynamicSnippetContentV1
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#snippetid" title="SnippetId">SnippetId</a>: <i>String</i>
</pre>

## Properties

#### Content

The VCL code that specifies exactly what the snippet does.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

The ID of the service that the dynamic snippet belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnippetId

The ID of the dynamic snippet that the content belong to.

_Required_: Yes

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

