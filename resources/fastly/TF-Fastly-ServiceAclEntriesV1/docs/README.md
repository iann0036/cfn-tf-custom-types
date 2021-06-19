# TF::Fastly::ServiceAclEntriesV1

Defines a set of Fastly ACL entries that can be used to populate a service ACL.  This resource will populate an ACL with the entries and will track their state.

~> **Warning:** Terraform will take precedence over any changes you make in the UI or API. Such changes are likely to be reversed if you run Terraform again.  

If Terraform is being used to populate the initial content of an ACL which you intend to manage via API or UI, then the lifecycle `ignore_changes` field can be used with the resource.  An example of this configuration is provided below.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Fastly::ServiceAclEntriesV1",
    "Properties" : {
        "<a href="#aclid" title="AclId">AclId</a>" : <i>String</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#entry" title="Entry">Entry</a>" : <i>[ <a href="entrydefinition.md">EntryDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Fastly::ServiceAclEntriesV1
Properties:
    <a href="#aclid" title="AclId">AclId</a>: <i>String</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#entry" title="Entry">Entry</a>: <i>
      - <a href="entrydefinition.md">EntryDefinition</a></i>
</pre>

## Properties

#### AclId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entry

_Required_: No

_Type_: List of <a href="entrydefinition.md">EntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

