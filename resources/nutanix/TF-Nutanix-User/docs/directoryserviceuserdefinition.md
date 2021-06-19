# TF::Nutanix::User DirectoryServiceUserDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#userprincipalname" title="UserPrincipalName">UserPrincipalName</a>" : <i>String</i>,
    "<a href="#directoryservicereference" title="DirectoryServiceReference">DirectoryServiceReference</a>" : <i>[ <a href="directoryservicereferencedefinition.md">DirectoryServiceReferenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#userprincipalname" title="UserPrincipalName">UserPrincipalName</a>: <i>String</i>
<a href="#directoryservicereference" title="DirectoryServiceReference">DirectoryServiceReference</a>: <i>
      - <a href="directoryservicereferencedefinition.md">DirectoryServiceReferenceDefinition</a></i>
</pre>

## Properties

#### UserPrincipalName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryServiceReference

_Required_: No

_Type_: List of <a href="directoryservicereferencedefinition.md">DirectoryServiceReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

