# TF::AVI::Certificatemanagementprofile

The CertificateManagementProfile resource allows the creation and management of Avi CertificateManagementProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Certificatemanagementprofile",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#runscriptref" title="RunScriptRef">RunScriptRef</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#scriptparams" title="ScriptParams">ScriptParams</a>" : <i>[ <a href="scriptparamsdefinition.md">ScriptParamsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Certificatemanagementprofile
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#runscriptref" title="RunScriptRef">RunScriptRef</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#scriptparams" title="ScriptParams">ScriptParams</a>: <i>
      - <a href="scriptparamsdefinition.md">ScriptParamsDefinition</a></i>
</pre>

## Properties

#### Name

Name of the pki profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunScriptRef

Alert script config object for certificate management profile. It is a reference to an object of type alertscriptconfig. Field introduced in 20.1.3.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptParams

_Required_: No

_Type_: List of <a href="scriptparamsdefinition.md">ScriptParamsDefinition</a>

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
