# Terraform::Linode::Stackscript

Provides a Linode StackScript resource.  This can be used to create, modify, and delete Linode StackScripts.  StackScripts are private or public managed scripts which run within an instance during startup.  StackScripts can include variables whose values are specified when the Instance is created.  

For more information, see [Automate Deployment with StackScripts](https://www.linode.com/docs/platform/stackscripts/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#tag/StackScripts).

The Linode Guide, [Deploy a WordPress Site Using Terraform and Linode StackScripts](https://www.linode.com/docs/applications/configuration-management/deploy-a-wordpress-site-using-terraform-and-linode-stackscripts/), shows how a public StackScript can be used to provision a Linode Instance.   The guide, [Create a Terraform Module](https://www.linode.com/docs/applications/configuration-management/create-terraform-module/), demonstrates StackScript use through a wrapping module.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Linode::Stackscript",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#images" title="Images">Images</a>" : <i>[ String, ... ]</i>,
        "<a href="#ispublic" title="IsPublic">IsPublic</a>" : <i>Boolean</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#revnote" title="RevNote">RevNote</a>" : <i>String</i>,
        "<a href="#script" title="Script">Script</a>" : <i>String</i>,
        "<a href="#userdefinedfields" title="UserDefinedFields">UserDefinedFields</a>" : <i>[ <a href="userdefinedfields.md">UserDefinedFields</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Linode::Stackscript
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#images" title="Images">Images</a>: <i>
      - String</i>
    <a href="#ispublic" title="IsPublic">IsPublic</a>: <i>Boolean</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#revnote" title="RevNote">RevNote</a>: <i>String</i>
    <a href="#script" title="Script">Script</a>: <i>String</i>
    <a href="#userdefinedfields" title="UserDefinedFields">UserDefinedFields</a>: <i>
      - <a href="userdefinedfields.md">UserDefinedFields</a></i>
</pre>

## Properties

#### Description

A description for the StackScript.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Images

An array of Image IDs representing the Images that this StackScript is compatible for deploying with.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPublic

This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `is_public` forces the creation of a new StackScript*.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The StackScript's label is for display purposes only.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevNote

This field allows you to add notes for the set of revisions made to this StackScript.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

The script to execute when provisioning a new Linode with this StackScript.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDefinedFields

_Required_: No

_Type_: List of <a href="userdefinedfields.md">UserDefinedFields</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Created

Returns the <code>Created</code> value.

#### DeploymentsActive

Returns the <code>DeploymentsActive</code> value.

#### DeploymentsTotal

Returns the <code>DeploymentsTotal</code> value.

#### Updated

Returns the <code>Updated</code> value.

#### UserGravatarId

Returns the <code>UserGravatarId</code> value.

#### Username

Returns the <code>Username</code> value.

