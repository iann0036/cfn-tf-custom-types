# TF::CheckPoint::ManagementInstallDatabase

This command resource allows you to execute Check Point Install Database.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementInstallDatabase",
    "Properties" : {
        "<a href="#targets" title="Targets">Targets</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementInstallDatabase
Properties:
    <a href="#targets" title="Targets">Targets</a>: <i>
      - String</i>
</pre>

## Properties

#### Targets

Check Point host(s) with one or more Management Software Blades enabled. The targets can be identified by their name or unique identifier.targets blocks are documented below.

_Required_: Yes

_Type_: List of String

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

#### Tasks

Collection of asynchronous task unique identifiers.

